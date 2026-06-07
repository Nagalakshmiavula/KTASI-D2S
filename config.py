# KTASI-D2S/config.py

from pathlib import Path


PROJECT_NAME = "KTASI-D2S"

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent

DATA_DIR = ROOT_DIR / "datasets"
TINY_IMAGENET_DIR = DATA_DIR / "tiny_imagenet"

CHECKPOINT_DIR = ROOT_DIR / "checkpoints"
RESULTS_DIR = ROOT_DIR / "results"
LOG_DIR = ROOT_DIR / "logs"

TRAIN_SPLIT_FILE = DATA_DIR / "train.txt"
VAL_SPLIT_FILE = DATA_DIR / "val.txt"
TEST_SPLIT_FILE = DATA_DIR / "test.txt"

# -----------------------------------------------------------------------------
# Reproducibility
# -----------------------------------------------------------------------------

SEED = 42

# -----------------------------------------------------------------------------
# Dataset
# -----------------------------------------------------------------------------

IMAGE_SIZE = 256

NUM_CHANNELS = 3

TRAIN_SPLIT = 0.70
VAL_SPLIT = 0.15
TEST_SPLIT = 0.15

NUM_WORKERS = 4

PIN_MEMORY = True

# -----------------------------------------------------------------------------
# Training
# -----------------------------------------------------------------------------

BATCH_SIZE = 16

LEARNING_RATE = 1e-4

WEIGHT_DECAY = 1e-5

MIXED_PRECISION = True

# -----------------------------------------------------------------------------
# Stage Training
# -----------------------------------------------------------------------------

EPOCHS_STAGE_A = 50
EPOCHS_STAGE_B = 100
EPOCHS_STAGE_C = 50

TOTAL_EPOCHS = (
    EPOCHS_STAGE_A
    + EPOCHS_STAGE_B
    + EPOCHS_STAGE_C
)

# -----------------------------------------------------------------------------
# Diffusion
# -----------------------------------------------------------------------------

DIFFUSION_STEPS = 16

BETA_START = 1e-4
BETA_END = 2e-2

DIFFUSION_SCHEDULE = "cosine"

# -----------------------------------------------------------------------------
# KTASI
# -----------------------------------------------------------------------------

KEY_DIM = 128

KEY_EMBED_DIM = 256

FUSION_DIM = 512

KTASI_INJECTION_STEPS = [16, 12, 8, 4]

# -----------------------------------------------------------------------------
# Latent Space
# -----------------------------------------------------------------------------

LATENT_CHANNELS = 8

FEATURE_CHANNELS = 64

# -----------------------------------------------------------------------------
# Validation
# -----------------------------------------------------------------------------

VALIDATION_INTERVAL = 100

SAVE_BEST_MODEL = True

# -----------------------------------------------------------------------------
# Metrics
# -----------------------------------------------------------------------------

PRIMARY_METRIC = "secret_ssim"
