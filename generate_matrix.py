import os

# The ultimate dynamic SVG engine with sequential boot-up animations
svg_code = """<svg width="900" height="400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Glowing Neon Filter -->
    <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    
    <!-- Heatmap Gradients -->
    <linearGradient id="heat-high" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00ffcc" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#004d00" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="heat-low" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f1923" stop-opacity="1"/>
      <stop offset="100%" stop-color="#16202b" stop-opacity="1"/>
    </linearGradient>
  </defs>

  <style>
    /* Global Styles */
    .bg-main { fill: #07090c; }
    .pane { fill: #0d1117; stroke: #30363d; stroke-width: 1.5; rx: 8; }
    .text-base { font-family: 'Courier New', monospace; font-size: 13px; }
    
    /* Terminal Styles */
    .term-header { fill: #8b949e; font-weight: bold; font-size: 14px; }
    .term-text { fill: #c9d1d9; }
    .term-highlight { fill: #00ffcc; font-weight: bold; }
    .term-accent { fill: #ff7b72; }
    
    /* Matrix Styles */
    .matrix-title { fill: #ffffff; font-size: 16px; font-weight: bold; font-family: 'Courier New', monospace; letter-spacing: 2px; }
    .matrix-label { fill: #8b949e; font-size: 12px; font-weight: bold; font-family: 'Courier New', monospace; }
    .matrix-val { fill: #ffffff; font-size: 22px; font-weight: bold; font-family: 'Courier New', monospace; }
    .matrix-cell { stroke: #30363d; stroke-width: 1; rx: 4; }
    
    /* Animations */
    .typing-line { opacity: 0; animation: typeIn 0.1s forwards; }
    .fade-in { opacity: 0; animation: fadeIn 1.5s ease-out forwards; }
    .pulse { animation: pulseOpacity 2s infinite; }
    
    /* Staggered Delays for Boot-up Sequence */
    .delay-1 { animation-delay: 0.5s; }
    .delay-2 { animation-delay: 1.2s; }
    .delay-3 { animation-delay: 1.9s; }
    .delay-4 { animation-delay: 2.6s; }
    .delay-5 { animation-delay: 3.3s; }
    .delay-matrix { animation-delay: 4.0s; }

    @keyframes typeIn { to { opacity: 1; } }
    @keyframes fadeIn { to { opacity: 1; } }
    @keyframes pulseOpacity { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
  </style>

  <!-- Background -->
  <rect width="100%" height="100%" class="bg-main"/>

  <!-- ================= LEFT PANE: TERMINAL ================= -->
  <rect x="20" y="20" width="410" height="360" class="pane"/>
  
  <!-- macOS Buttons -->
  <circle cx="45" cy="40" r="6" fill="#ff5f56"/>
  <circle cx="65" cy="40" r="6" fill="#ffbd2e"/>
  <circle cx="85" cy="40" r="6" fill="#27c93f"/>
  <text x="110" y="45" class="text-base term-header">harjas@quant-core:~</text>

  <!-- Terminal Boot Sequence -->
  <g class="text-base">
    <text x="40" y="90" class="typing-line delay-1 term-text">> initializing neural architecture...</text>
    <text x="40" y="120" class="typing-line delay-2 term-text">> loading backbone: <tspan class="term-highlight">MobileNetV2</tspan></text>
    <text x="40" y="150" class="typing-line delay-3 term-text">> setting framework: <tspan class="term-highlight">TensorFlow Keras</tspan></text>
    <text x="40" y="180" class="typing-line delay-4 term-text">> injecting NLP: <tspan class="term-accent">VADER Sentiment</tspan></text>
    <text x="40" y="210" class="typing-line delay-4 term-text">> connecting live data pipelines...</text>
    <text x="40" y="260" class="typing-line delay-5 term-text">> status: <tspan class="term-highlight pulse" filter="url(#neon-glow)">optimizing the climb...</tspan></text>
    <text x="40" y="290" class="typing-line delay-5 term-text">> executing: alpha_matrix.sh</text>
  </g>

  <!-- ================= RIGHT PANE: CONFUSION MATRIX ================= -->
  <rect x="450" y="20" width="430" height="360" class="pane"/>
  
  <g class="fade-in delay-matrix">
    <text x="480" y="55" class="matrix-title">STRATEGY CONFUSION MATRIX</text>
    <line x1="480" y1="70" x2="850" y2="70" stroke="#30363d" stroke-width="2"/>

    <!-- Matrix Grid Container -->
    <g transform="translate(530, 110)">
      <!-- Column Labels -->
      <text x="35" y="-15" class="matrix-label">BULLISH</text>
      <text x="140" y="-15" class="matrix-label">BEARISH</text>
      <text x="245" y="-15" class="matrix-label">MEAN_REV</text>

      <!-- Row Labels -->
      <text x="-60" y="45" class="matrix-label">BULLISH</text>
      <text x="-60" y="135" class="matrix-label">BEARISH</text>
      <text x="-60" y="225" class="matrix-label">MEAN_REV</text>

      <!-- Row 1 -->
      <rect x="0" y="0" width="90" height="80" class="matrix-cell" fill="url(#heat-high)"/>
      <text x="25" y="50" class="matrix-val">.92</text>
      
      <rect x="100" y="0" width="90" height="80" class="matrix-cell" fill="url(#heat-low)"/>
      <text x="25" y="50" transform="translate(100,0)" class="matrix-val" fill="#8b949e">.04</text>
      
      <rect x="200" y="0" width="90" height="80" class="matrix-cell" fill="url(#heat-low)"/>
      <text x="25" y="50" transform="translate(200,0)" class="matrix-val" fill="#8b949e">.01</text>

      <!-- Row 2 -->
      <rect x="0" y="90" width="90" height="80" class="matrix-cell" fill="url(#heat-low)"/>
      <text x="25" y="140" class="matrix-val" fill="#8b949e">.05</text>
      
      <rect x="100" y="90" width="90" height="80" class="matrix-cell" fill="url(#heat-high)"/>
      <text x="25" y="140" transform="translate(100,0)" class="matrix-val">.89</text>
      
      <rect x="200" y="90" width="90" height="80" class="matrix-cell" fill="url(#heat-low)"/>
      <text x="25" y="140" transform="translate(200,0)" class="matrix-val" fill="#8b949e">.04</text>

      <!-- Row 3 -->
      <rect x="0" y="180" width="90" height="80" class="matrix-cell" fill="url(#heat-low)"/>
      <text x="25" y="230" class="matrix-val" fill="#8b949e">.02</text>
      
      <rect x="100" y="180" width="90" height="80" class="matrix-cell" fill="url(#heat-low)"/>
      <text x="25" y="230" transform="translate(100,0)" class="matrix-val" fill="#8b949e">.03</text>
      
      <rect x="200" y="180" width="90" height="80" class="matrix-cell" fill="url(#heat-high)"/>
      <text x="25" y="230" transform="translate(200,0)" class="matrix-val">.94</text>
    </g>
  </g>
</svg>
"""

with open('quant_dashboard.svg', 'w') as f:
    f.write(svg_code)
