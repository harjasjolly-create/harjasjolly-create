import os

# The Fun "Dev Life" Max-Glow Engine
svg_code = """<svg width="900" height="400" xmlns="http://www.w3.org/2000/svg">
  <style>
    /* Global Deep Space Background */
    .bg-main { fill: #040608; }
    .pane { fill: #090c10; stroke: #161b22; stroke-width: 2; rx: 8; }
    
    /* Base Fonts */
    .text-base { font-family: 'Courier New', monospace; font-size: 13px; }
    
    /* =================== THE GLOW FX =================== */
    .neon-text-green { 
        fill: #00ffcc; font-weight: bold;
        text-shadow: 0 0 5px #00ffcc, 0 0 15px #00ffcc, 0 0 25px #00ffcc; 
    }
    .neon-text-white { 
        fill: #ffffff; font-weight: bold;
        text-shadow: 0 0 5px #ffffff, 0 0 12px #00ffcc; 
    }
    
    /* Glowing Matrix Boxes */
    .cell-high { 
        fill: rgba(0, 255, 204, 0.05); stroke: #00ffcc; stroke-width: 2; rx: 4;
        filter: drop-shadow(0 0 8px rgba(0, 255, 204, 0.8)); 
    }
    .cell-low { fill: #0d1117; stroke: #1e252e; stroke-width: 1; rx: 4; }
    
    /* Matrix Values */
    .val-high { 
        fill: #ffffff; font-size: 24px; font-weight: bold; font-family: 'Courier New', monospace; 
        text-shadow: 0 0 8px #ffffff, 0 0 20px #00ffcc; 
    }
    .val-low { fill: #30363d; font-size: 20px; font-family: 'Courier New', monospace; }
    .term-text { fill: #8b949e; }
    .term-accent { fill: #ff7b72; text-shadow: 0 0 8px #ff7b72; }
    
    /* =================== ANIMATIONS =================== */
    .typing-line { opacity: 0; animation: typeIn 0.1s forwards; }
    .fade-in { opacity: 0; animation: fadeIn 1s ease-out forwards; }
    .pulse-glow { animation: pulseGlow 2s infinite alternate; }
    
    /* Staggered Boot Sequence */
    .delay-1 { animation-delay: 0.4s; }
    .delay-2 { animation-delay: 0.8s; }
    .delay-3 { animation-delay: 1.2s; }
    .delay-4 { animation-delay: 1.6s; }
    .delay-5 { animation-delay: 2.0s; }
    .delay-matrix { animation-delay: 2.5s; }

    @keyframes typeIn { to { opacity: 1; } }
    @keyframes fadeIn { to { opacity: 1; } }
    @keyframes pulseGlow { 
        0% { filter: drop-shadow(0 0 2px #00ffcc); } 
        100% { filter: drop-shadow(0 0 15px #00ffcc); } 
    }
  </style>

  <!-- Background -->
  <rect width="100%" height="100%" class="bg-main"/>

  <!-- ================= LEFT PANE: TERMINAL ================= -->
  <rect x="20" y="20" width="410" height="360" class="pane"/>
  
  <!-- macOS Buttons -->
  <circle cx="45" cy="40" r="6" fill="#ff5f56"/>
  <circle cx="65" cy="40" r="6" fill="#ffbd2e"/>
  <circle cx="85" cy="40" r="6" fill="#27c93f"/>
  <text x="110" y="45" class="text-base" fill="#8b949e" font-weight="bold">harjas@dev-core:~</text>

  <!-- Terminal Boot Sequence -->
  <g class="text-base">
    <text x="40" y="90" class="typing-line delay-1 term-text">> system_check: <tspan class="term-accent">coffee_levels_critical</tspan></text>
    <text x="40" y="130" class="typing-line delay-2 term-text">> dependencies: <tspan class="neon-text-green">stack_overflow, caffeine</tspan></text>
    <text x="40" y="170" class="typing-line delay-3 term-text">> task_1: <tspan class="neon-text-white">write_clean_code</tspan></text>
    <text x="40" y="210" class="typing-line delay-4 term-text">> task_2: <tspan class="neon-text-white">fix_one_bug</tspan></text>
    <text x="40" y="270" class="typing-line delay-5 term-text">> outcome: <tspan class="term-accent pulse-glow">created_three_more_bugs</tspan></text>
    <text x="40" y="310" class="typing-line delay-5 term-text">> status: <tspan class="neon-text-green pulse-glow">works_on_my_machine</tspan></text>
  </g>

  <!-- ================= RIGHT PANE: CONFUSION MATRIX ================= -->
  <rect x="450" y="20" width="430" height="360" class="pane"/>
  
  <g class="fade-in delay-matrix">
    <text x="480" y="55" class="neon-text-green" font-size="16" letter-spacing="2">DEV LIFE CONFUSION MATRIX</text>
    <line x1="480" y1="70" x2="850" y2="70" stroke="#161b22" stroke-width="2"/>

    <!-- Matrix Grid Container -->
    <g transform="translate(530, 110)">
      <!-- Column Labels (EXPECTED) -->
      <text x="45" y="-15" class="text-base neon-text-white" font-size="12">SLEEP</text>
      <text x="150" y="-15" class="text-base neon-text-white" font-size="12">CODE</text>
      <text x="245" y="-15" class="text-base neon-text-white" font-size="12">DEBUG</text>

      <!-- Row Labels (ACTUAL) -->
      <text x="-50" y="45" class="text-base neon-text-white" font-size="12">SLEEP</text>
      <text x="-50" y="135" class="text-base neon-text-white" font-size="12">CODE</text>
      <text x="-50" y="225" class="text-base neon-text-white" font-size="12">DEBUG</text>

      <!-- Row 1 (Actual SLEEP) -->
      <rect x="0" y="0" width="90" height="80" class="cell-low"/>
      <text x="25" y="50" class="val-low">.05</text>
      
      <rect x="100" y="0" width="90" height="80" class="cell-low"/>
      <text x="25" y="50" transform="translate(100,0)" class="val-low">.02</text>
      
      <rect x="200" y="0" width="90" height="80" class="cell-low"/>
      <text x="25" y="50" transform="translate(200,0)" class="val-low">.01</text>

      <!-- Row 2 (Actual CODE) -->
      <!-- Joke: Planned to Sleep, actually coded -->
      <rect x="0" y="90" width="90" height="80" class="cell-high pulse-glow"/>
      <text x="25" y="140" class="val-high">.85</text>
      
      <rect x="100" y="90" width="90" height="80" class="cell-low"/>
      <text x="25" y="140" transform="translate(100,0)" class="val-low">.10</text>
      
      <rect x="200" y="90" width="90" height="80" class="cell-low"/>
      <text x="25" y="140" transform="translate(200,0)" class="val-low">.05</text>

      <!-- Row 3 (Actual DEBUG) -->
      <rect x="0" y="180" width="90" height="80" class="cell-low"/>
      <text x="25" y="230" class="val-low">.10</text>
      
      <!-- Joke: Planned to Code, actually just debugged -->
      <rect x="100" y="180" width="90" height="80" class="cell-high pulse-glow"/>
      <text x="25" y="230" transform="translate(100,0)" class="val-high">.88</text>
      
      <rect x="200" y="180" width="90" height="80" class="cell-high pulse-glow"/>
      <text x="25" y="230" transform="translate(200,0)" class="val-high">.94</text>
    </g>
  </g>
</svg>
"""

with open('quant_dashboard.svg', 'w') as f:
    f.write(svg_code)
