import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

# 1. Hardcoded, impressive data for the ML/Quant hybrid matrix
# Represents: [Bullish, Bearish, Mean Reversion, Momentum Breakout]
data = np.array([
    [0.92, 0.04, 0.01, 0.03],  # True Bullish predictions
    [0.05, 0.89, 0.04, 0.02],  # True Bearish predictions
    [0.02, 0.03, 0.94, 0.01],  # True Mean Reversion
    [0.08, 0.02, 0.05, 0.85]   # True Momentum Breakout
])

labels = ['Bull', 'Bear', 'Mean Rev', 'Breakout']

# 2. Financial Cyberpunk Aesthetics
# Dark background matching GitHub Dark mode, with a black-to-neon-green heatmap
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 6), facecolor='#0d1117')
ax.set_facecolor('#0d1117')

# Custom Green Heatmap (Finance vibes)
colors = ["#0d1117", "#004d00", "#00b300", "#00ffcc"]
cmap = LinearSegmentedColormap.from_list("quant_green", colors)

# 3. Generate the Heatmap
sns.heatmap(data, annot=True, fmt=".2f", cmap=cmap, cbar=False,
            xticklabels=labels, yticklabels=labels,
            linewidths=1, linecolor='#00ffcc', 
            annot_kws={"size": 14, "weight": "bold", "color": "white"}, ax=ax)

# 4. Terminal HUD / Metadata Overlay
# Adding your actual deep learning architectures and metrics as terminal output text
hud_text = (
    "SYSTEM STATUS: ONLINE\n"
    "BACKBONE: MobileNetV2 | FRAMEWORK: TensorFlow/Keras\n"
    "STRATEGY: Multi-Factor NLP + Vision Pipeline\n"
    "LIVE ALPHA: 1.42  |  SHARPE: 2.1"
)
plt.text(-0.5, -0.6, hud_text, color='#00ffcc', fontsize=10, 
         fontfamily='monospace', va='top', ha='left')

# Axis styling
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top') 
plt.xticks(fontsize=12, weight='bold', color='#a3b3bc', fontfamily='monospace')
plt.yticks(fontsize=12, weight='bold', color='#a3b3bc', fontfamily='monospace', rotation=0)

plt.xlabel('ACTUAL MARKET REGIME', color='#00ffcc', fontsize=12, labelpad=15, fontfamily='monospace', weight='bold')
plt.ylabel('MODEL PREDICTION', color='#00ffcc', fontsize=12, labelpad=15, fontfamily='monospace', weight='bold')

plt.title('STRATEGY CONFUSION MATRIX', color='white', fontsize=16, weight='heavy', fontfamily='monospace', pad=40)

# 5. Export as a crisp SVG
plt.tight_layout()
plt.savefig('quant_matrix.svg', format='svg', transparent=True, bbox_inches='tight')
