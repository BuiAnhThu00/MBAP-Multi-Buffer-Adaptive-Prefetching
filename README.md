## MBAP Algorithm (Multi-Buffer Adaptive Prefetching)

The MBAP algorithm is designed to optimize short-form video streaming platforms by intelligently managing multiple playback buffers and adaptively prefetching video segments. Each upcoming video in the feed is assigned its own buffer, which is dynamically updated based on network throughput and user behavior. MBAP adjusts the number of videos to prefetch according to real-time conditions: if users scroll quickly, more videos are prefetched; if they linger, fewer are prefetched to save bandwidth. Optionally, machine learning can be integrated to predict which videos are most likely to be watched next, prioritizing their prefetching. This approach minimizes startup delay, rebuffering events, and buffer waste, resulting in a smoother and more efficient streaming experience even under fluctuating network conditions.

---

### Operating Principles

- **Multi-buffer allocation:** Each video in the user’s feed is assigned a separate buffer to prevent interruptions caused by rapid navigation.
- **Real-time throughput monitoring:** Network speed is continuously measured to estimate download time and manage buffer size.
- **Adaptive segment prefetching:** The algorithm dynamically decides how many upcoming videos to prefetch, scaling with user scroll speed and interaction patterns.
- **User behavior awareness:** Prefetching strategy adapts if users linger longer or skip quickly, optimizing resource usage.
- **Machine learning integration (optional):** Predicts which videos are likely to be played next, allowing targeted prefetching for maximum efficiency.
- **QoE optimization:** MBAP tracks startup delay, rebuffering, and buffer waste, constantly tuning its parameters to maximize Quality of Experience.
