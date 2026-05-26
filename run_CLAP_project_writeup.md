# Listening to the City: Testing CLAP for Urban Sound Classification

*A rough draft — feel free to cut, rearrange, and rewrite. ~2000 words.*

## Where this started

Sensemakers is an Amsterdam-based community of people who build things with sensors, networks, and increasingly, machine learning. The group has been around since the early days of the IoT wave, and one of its longest-running threads is a project on **urban sounds** — the idea that the noise around us in a city carries real information, and that if we can capture and classify it, we get a much richer picture of what's going on in a neighbourhood than we'd ever get from looking at a map or a traffic count.

We started the urban sounds work in 2019. The original motivation was noise pollution: Amsterdam, like every other dense European city, has a noise problem, and the problem is not evenly distributed. A street with mopeds and shouting at 2am is a different place than a street with trams and cyclists. Standard noise meters tell you *how loud* something is in decibels, but they don't tell you *what* it is. A leaf blower at 75 dB and a saxophone busker at 75 dB are very different problems — or, in the second case, not a problem at all.

So the goal from the beginning was classification, not just measurement. What is making the noise, when, where, and how often? With enough small devices distributed across a neighbourhood, you'd start to build a soundscape map — not just a heatmap of loudness, but a description of acoustic life.

For years we worked with custom-trained audio classifiers, mostly built on convolutional neural networks fed with spectrograms. They worked, but they had the classic ML problem: every new sound class you wanted to detect required new labelled training data, retraining, evaluation, deployment. The world has more sounds in it than we could ever label.

This is where CLAP came in.

## What CLAP is, and why it changes the picture

CLAP stands for **Contrastive Language-Audio Pretraining**. It's a neural network trained on a huge variety of (audio, text) pairs — clips of sound paired with descriptions of what they are. The training is contrastive: the model learns to put a piece of audio and its matching text label close together in a shared embedding space, and to push non-matching pairs apart. If you've seen CLIP for images and captions, CLAP is the audio equivalent. Same idea, different modality.

The practical consequence is that CLAP doesn't have a fixed set of output classes. You give it an audio clip and a list of candidate text labels — *"a dog barking"*, *"a tram passing"*, *"children playing"*, *"a leaf blower"* — and the model tells you which label fits best. You can change the labels at inference time, without retraining anything. You can add a new class by just typing a new sentence.

For a project like ours, this is enormous. We can adapt the labels to a specific location ("near the canal, listen for boat engines and seagulls"; "near the school, listen for children and ball games") without going through a fresh data collection cycle every time. The model is doing zero-shot classification, and for many urban sounds it does it surprisingly well.

There are several CLAP models published by LAION on Hugging Face. We tested two of them:

1. `larger_clap_music_and_speech`
2. `larger_clap_general`

The naming hints at the training mix. The first is tuned toward music and speech, which sounds useful for a city — there is plenty of both — but in our experiments the second one, the general-purpose model, consistently gave better results across the messy mix of urban sounds we care about. So `larger_clap_general` became our default.

Useful references for anyone digging in:
- [CLAP on Hugging Face](https://huggingface.co/laion/larger_clap_general)
- [The CLAP paper on arXiv](https://arxiv.org/abs/2211.06687)

## The dataset

To evaluate the model we needed a dataset that actually looks like Amsterdam, not like generic North American acoustic-scene benchmarks. We assembled a small but focused set called **UrbanSoundsNew**, hosted on the Hugging Face Hub. It contains 216 samples across nine classes of urban audio events — things like vehicles, voices, machinery, and other sounds typical for the city.

216 samples is not large, and we're not claiming it is. The dataset is meant for *testing* and *demonstrating* a zero-shot model, not for training one. The whole point of CLAP is that you don't need a huge labelled dataset to get started; you need a small, well-curated one to verify that the model behaves the way you expect it to in your domain.

The dataset lives here: [UrbanSoundsNew on Hugging Face](https://huggingface.co/datasets/UrbanSounds/UrbanSoundsNew).

## Notebooks: first contact with the model

The first folder in the repo (`1_test_CLAP_notebooks`) is where we did the initial exploration. There are a handful of Jupyter notebooks, all using the Hugging Face `transformers` library, which makes loading and running CLAP a few lines of Python.

The notebooks cover progressively more interesting things:

- **UrbanSoundsII dataset with CLAP.ipynb** — the baseline. Load the model, load the dataset, run inference, look at how often the top predicted label matches the ground truth. This is the "does it work at all" notebook, and the answer was yes, encouragingly often.
- **CLAP embeddings.ipynb** — instead of asking the model for a label, we ask it for the **audio embedding**: a high-dimensional vector representing the clip in the model's learned space. Once you have embeddings, you can do similarity search (find the five clips most acoustically similar to this one), and you can do dimensionality reduction with PCA or t-SNE to visualise the dataset in 2D. The visualisations tell you a lot about how the model "sees" your data: classes that cluster tightly are easy for the model; classes that smear into each other are the ones you'll have trouble with.
- **Real UrbanSoundsSamples with CLAP.ipynb** — moving from the curated dataset to actual field recordings. This is where the model meets the messiness of real audio: wind on the microphone, traffic in the background, overlapping events.
- **Visualising the UrbanSoundsSamples with CLAP embeddings.ipynb** — still in progress, but the idea is to project real-world recordings into the same embedding space and see whether the structure of the soundscape over time is visible. Does the morning sound different from the evening? Does the canal side cluster differently from the square?
- **UrbanSounds_audio_pipeline.ipynb** — the glue: a notebook that pulls together loading, preprocessing, inference, and output into a runnable pipeline rather than a series of isolated cells.

The notebooks aren't a polished library. They are scratch paper. They are how we figured out what worked.

## From notebook to device: running CLAP on a Raspberry Pi

A model that only runs on a laptop is interesting. A model that runs on a small, cheap, low-power device that you can mount on a lamppost and forget about is *useful*. The second folder in the repo (`2_python_CLAP`) is the move from notebook to deployment.

The latest production script is **`urban_sounds_3.5.py`**. The version number tells you it took a few iterations to get right. The script captures audio from a microphone, runs CLAP locally on the Pi, classifies the clip against a configurable list of labels, and publishes the result over MQTT. MQTT credentials live in a `config.py` file that is — obviously — not committed to the repository.

One small but important piece of architecture is `sound_scapes.py`. Different locations need different label sets. A microphone near a marina is going to hear different things than a microphone next to a school playground, and there's no point asking the model "is this a horse" if there are no horses for kilometres. `sound_scapes.py` stores location-specific label lists. Right now there's one location defined, **Marineterrein** — a former naval terrain in central Amsterdam that's being redeveloped as a kind of urban innovation district, and is one of our test sites. Adding a new location means adding a new entry: a name, a set of candidate sound labels, optional weights or filters. The script reads from this file at startup.

There are a handful of settings inside the script that you'll want to check before running — sample rate, clip length, model variant, MQTT topic. We don't pretend it's a polished CLI tool. It's a working device script.

Tucked inside this folder is a `cpu_usage/` subfolder containing a short, vibe-coded helper script that samples the CPU load while the classifier is running and produces a matplotlib PNG of the result. This sounds trivial but it's actually one of the more important things in the project. Running a transformer-based model on a Raspberry Pi is not free; if the CPU is pinned at 100% for the entire classification window, you're either going to overheat the device, miss audio, or both. The CPU graphs let us see, at a glance, whether the current settings are sustainable for continuous deployment, and they're how we sized the inference batch and the gap between samples.

## Stress test: how much noise can the model take?

The third folder (`3_tests_whitenoise_wind_db`) is one of my favourites, and it answers a question that any field-deployment person asks immediately: *what happens when the microphone is in a windy place and the audio is half static?*

We took clean samples from the dataset and progressively added white noise — 10%, 25%, 50%, all the way up to 100% — and then re-ran CLAP and looked at whether the classifications still held. The notebooks are honest, vibe-coded experiments, not formal evaluations, but the result was striking enough to call out in the README: **even with 100% white noise added, the audio classification is still good**.

That's not what we expected. We expected gradual degradation. What we got was a model that, for the urban-sound classes we care about, is remarkably robust to additive noise. We have a few hypotheses for why — CLAP's training data probably included plenty of noisy real-world audio, and the contrastive objective may reward the model for focusing on the salient acoustic features rather than the overall signal-to-noise ratio — but we haven't tested any of them rigorously yet.

The practical implication is real, though: we can deploy these microphones outdoors, on lampposts, in weather, without an expensive enclosure, and still expect usable classifications.

## Documentation, video, and explainability

Folder four (`4_CLAP_documentation`) is a small archive of presentation material: a PowerPoint, some images, some short clips. We've given a couple of talks about this work at Sensemakers meetups and elsewhere, and the slides live here for anyone who wants to pick them up.

There's also a YouTube video walking through what CLAP is and how we use it: [https://youtu.be/dPcVhHVIoIs](https://youtu.be/dPcVhHVIoIs).

The fifth folder (`5_explainability`) is more recent and more exploratory. Embeddings-based models are notoriously hard to interpret. If CLAP tells us "this is a tram", we'd like to know *why* — what in the audio led to that conclusion? This is the harder of the two open problems we're working on right now (the other being deployment at scale). There's no clean answer yet; the folder contains the experiments we're running.

## What we learned, and what's next

A few honest takeaways:

**The zero-shot promise is real.** We did not retrain anything. We loaded a pretrained model from Hugging Face, gave it our labels, and got useful classifications across nine urban sound categories. For a community project run by volunteers, this is the difference between "possible" and "impossible".

**General-purpose models beat specialised ones, at least here.** `larger_clap_general` outperformed `larger_clap_music_and_speech` on our data, even though the latter sounds, on paper, like it ought to be more relevant. The lesson is to test, not to assume from the name.

**Edge deployment is the bottleneck, not the model.** The Pi runs CLAP, but only just. CPU monitoring, careful sample scheduling, and a willingness to accept a few seconds of latency are all part of making this practical.

**Robustness to noise was a happy surprise.** This is the result that most changes our planning. It means cheaper deployment, less worry about microphone placement, and a real path to running these things permanently outdoors.

**What's missing is scale and interpretability.** One device on the Marineterrein is a prototype. A neighbourhood-wide network of devices, with dashboards, alerts, and explainability that a non-ML resident can read, is the actual product. That's where we're heading.

If you want to read the code, mess with the notebooks, or fork the repo: [github.com/MichielBontenbal/run_CLAP](https://github.com/MichielBontenbal/run_CLAP). Issues and pull requests welcome. The dataset is on Hugging Face. The model is on Hugging Face. None of this is locked away. The whole point of doing it in the open is that the next person — in Rotterdam, in Berlin, in Bogotá — can pick it up and listen to their own city.
