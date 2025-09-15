# MBAP-Multi-Buffer-Adaptive-Prefetching
Multi-Buffer Adaptive Prefetching (MBAP) Algorithm
Overview
The MBAP algorithm is designed to optimize short-form video streaming systems by intelligently managing multiple playback buffers and dynamically prefetching video segments. It aims to maximize user Quality of Experience (QoE) by minimizing startup delay, rebuffering events, and buffer waste, especially in environments with fluctuating network conditions and unpredictable user behavior.

Key Components
1. Multi-Buffer Management

Each video in the upcoming feed is assigned its own buffer, independent from others.
Buffers are updated individually based on the real-time network throughput and video playback progress.
This design prevents the common problem where a single buffer causes unnecessary rebuffering when users quickly scroll through multiple videos.
2. Throughput Monitoring

The algorithm continuously monitors network throughput over a sliding time window (W seconds).
Average throughput is calculated to predict segment download speed and adjust buffer filling accordingly.
3. Adaptive Segment Prefetching

MBAP dynamically determines how many upcoming videos (parameter: K_NEXT) should be prefetched.
If the user scrolls quickly, more videos are prefetched; if the user dwells longer, fewer videos are prefetched, saving bandwidth and memory.
Prefetching is performed at the segment level, so only essential parts of videos (e.g., startup segments) are buffered initially.
4. Machine Learning-Based Prediction (Optional)

User behavior (scroll speed, interaction history) is fed to a machine learning model to predict which videos are most likely to be played next.
The algorithm prioritizes prefetching for videos with higher predicted watch probabilities.
5. QoE-Oriented Buffer Control

MBAP tracks three main QoE metrics for each video:
Startup Delay: Time before playback begins.
Rebuffer Time: Total duration of playback interruptions due to empty buffer.
Buffer Waste: Amount of data buffered but not watched (e.g., if the user skips a video).
An aggregate QoE score is computed for performance evaluation and adaptive tuning.
Algorithm Steps
Initialization

For each video in the user feed, initialize an independent buffer.
Set default values for K_NEXT (e.g., 1–3), buffer thresholds, and segment duration (tau).
Startup Buffering

Prefetch the startup segments for the current and next K_NEXT videos.
Estimate download time using current throughput statistics.
Playback and Prefetching Loop

As the user watches a video, MBAP continues to prefetch segments for upcoming videos according to adaptive K_NEXT.
If a buffer runs empty during playback, record a rebuffer event and update QoE metrics.
Adaptive Adjustment

Periodically analyze user scroll behavior and network conditions.
Adjust K_NEXT or buffer thresholds to minimize rebuffering and buffer waste.
Machine Learning Integration (Optional)

Use real-time prediction to reorder or prioritize prefetching for videos with higher play probability.
Reallocate buffer resources adaptively.
QoE Evaluation

After playback, calculate startup delay, total rebuffer time, buffer waste, and aggregate QoE.
Use these metrics to fine-tune algorithm parameters for future sessions.
Advantages of MBAP
Resilient to Fast User Scrolling: Each video buffer is independent, so rapid feed navigation does not trigger excessive rebuffering.
Efficient Network Usage: Adaptive prefetching reduces unnecessary data download for videos unlikely to be watched.
Higher QoE: Startup delay and playback interruptions are minimized, leading to smoother viewing.
Expandable: The algorithm can be enhanced with user modeling, context-aware adjustments, and reinforcement learning.
Example Workflow
User opens their feed; MBAP initializes buffers for the first N videos.
As the user scrolls, MBAP observes scroll speed and adjusts K_NEXT.
If network speed drops, MBAP prioritizes prefetching startup segments and may reduce K_NEXT.
If the user lingers on a video, MBAP reallocates resources to buffer deeper segments for that video.
After the feed is consumed, MBAP reports individual video QoE metrics and overall system performance.
Summary:
MBAP is an advanced, adaptive algorithm for multi-video streaming platforms, integrating network monitoring, buffer management, and user behavior prediction to maximize playback quality and resource efficiency.
