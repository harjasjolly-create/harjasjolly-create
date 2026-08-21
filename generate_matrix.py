import os

# The Raw SVG Engine with embedded CSS for animations and glowing neon effects
svg_code = """<svg width="850" height="450" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg { fill: #090c10; }
    .window { fill: #161b22; stroke: #30363d; stroke-width: 2; rx: 10; }
    .neon-text { 
        font-family: 'Courier New', monospace; 
        fill: #00ffcc; 
        font-size: 16px; 
        font-weight: bold;
        text-shadow: 0 0 5px #00ffcc, 0 0 10px #00ffcc; 
    }
    .white-text { font-family: 'Courier New', monospace; fill: #c9d1d9; font-size: 14px; }
    .matrix-box { fill: #0d1117; stroke: #00ffcc; stroke-width: 1; }
    
    /* Blinking Cursor Animation */
    .cursor { animation: blink 1s step-end infinite; }
    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    
    /* Fade In Animation for Matrix Data */
    .fade-in { animation: fadeIn 2s ease-in forwards; opacity: 0; }
    @keyframes fadeIn { to { opacity: 1; } }
  </style>

  <!-- Background and Terminal Window -->
  <rect width="100%" height="100%" class="bg"/>
  <rect x="25" y="25" width="800" height="400" class="window"/>
  
  <!-- macOS Terminal Buttons -->
  <circle cx="50" cy="50" r="6" fill="#ff5f56"/>
  <circle cx="70" cy="50" r="6" fill="#ffbd2e"/>
  <circle cx="90" cy="50" r="6" fill="#27c93f"/>
  
  <!-- Header Text -->
  <text x="120" y="55" class="white-text" font-weight="bold">harjas@quant-server: ~/trading/models</text>

  <!-- Animated Terminal Typing -->
  <text x="50" y="100" class="neon-text">> EXECUTING: multi_factor_alpha.py <tspan class="cursor">_</tspan></text>
  <text x="50" y="130" class="white-text">> BACKBONE: MobileNetV2 | NLP: VADER</text>
  <text x="50" y="150" class="white-text">> STATUS: LIVE_EVALUATION</text>

  <!-- The Glowing Confusion Matrix -->
  <g class="fade-in" transform="translate(450, 100)">
    <!-- Headers -->
    <text x="60" y="-15" class="neon-text">BULL</text>
    <text x="140" y="-15" class="neon-text">BEAR</text>
    <text x="220" y="-15" class="neon-text">REV</text>
    <text x="-60" y="40" class="neon-text">BULL</text>
    <text x="-60" y="120" class="neon-text">BEAR</text>
    <text x="-60" y="200" class="neon-text">REV</text>

    <!-- Grid Boxes & Data -->
    <rect x="0" y="0" width="80" height="80" class="matrix-box" fill="#004d00"/>
    <text x="25" y="45" class="neon-text" font-size="20">.92</text>
    
    <rect x="80" y="0" width="80" height="80" class="matrix-box"/>
    <text x="105" y="45" class="white-text">.04</text>
    
    <rect x="160" y="0" width="80" height="80" class="matrix-box"/>
    <text x="185" y="45" class="white-text">.01</text>
    
    <!-- Row 2 -->
    <rect x="0" y="80" width="80" height="80" class="matrix-box"/>
    <text x="25" y="125" class="white-text">.05</text>
    
    <rect x="80" y="80" width="80" height="80" class="matrix-box" fill="#004d00"/>
    <text x="105" y="125" class="neon-text" font-size="20">.89</text>
    
    <rect x="160" y="80" width="80" height="80" class="matrix-box"/>
    <text x="185" y="125" class="white-text">.04</text>
    
    <!-- Row 3 -->
    <rect x="0" y="160" width="80" height="80" class="matrix-box"/>
    <text x="25" y="205" class="white-text">.02</text>
    
    <rect x="80" y="160" width="80" height="80" class="matrix-box"/>
    <text x="105" y="205" class="white-text">.03</text>
    
    <rect x="160" y="160" width="80" height="80" class="matrix-box" fill="#004d00"/>
    <text x="185" y="205" class="neon-text" font-size="20">.94</text>
  </g>

  <!-- Left Side Stats Panel -->
  <g class="fade-in">
      <rect x="50" y="200" width="300" height="150" class="matrix-box"/>
      <text x="65" y="230" class="neon-text">SYSTEM METRICS</text>
      <text x="65" y="260" class="white-text">PRECISION : 0.94</text>
      <text x="65" y="290" class="white-text">RECALL    : 0.91</text>
      <text x="65" y="320" class="white-text">SHARPE    : 2.14</text>
  </g>
</svg>
"""

with open('quant_matrix.svg', 'w') as f:
    f.write(svg_code)
