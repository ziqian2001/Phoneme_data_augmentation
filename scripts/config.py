#!/usr/bin/env python3

"""
Central configuration for the cross-lingual TTS experiment.
"""
import os

# ============================================================
# Base paths
# ============================================================
PROJECT_DIR = "/proj/uppmax2025-2-505/ziqian/experiment"
DATA_DIR = os.path.join(PROJECT_DIR, "data")

# ============================================================
# Language pair definitions
# Each pair: source (high-resource EN) → target (low-resource)
# ============================================================
LANGUAGE_PAIRS = {
    "en_sv": {
        "source_lang": "en",
        "target_lang": "sv",
        "source_corpus": "libritts",
        "target_corpus": "nst_swedish",
        # MFA output directories (containing .TextGrid files)
        "source_mfa_dir": os.path.join(DATA_DIR, "mfa_output", "en"),
        "target_mfa_dir": os.path.join(DATA_DIR, "mfa_output", "sv"),
        # Audio directories (containing .wav files)
        "source_audio_dir": os.path.join(DATA_DIR, "audio", "en"),
        "target_audio_dir": os.path.join(DATA_DIR, "audio", "sv"),
        # Configuration for data splits
        "target_train_n": 400,
        "target_test_n": 100,
        "source_n": 2000,
    },
    "en_ja": {
        "source_lang": "en",
        "target_lang": "ja",
        "source_corpus": "libritts",
        "target_corpus": "common_voice_ja",
        "source_mfa_dir": os.path.join(DATA_DIR, "mfa_output", "en"),
        "target_mfa_dir": os.path.join(DATA_DIR, "mfa_output", "ja"),
        "source_audio_dir": os.path.join(DATA_DIR, "audio", "en"),
        "target_audio_dir": os.path.join(DATA_DIR, "audio", "ja"),
        "target_train_n": 400,
        "target_test_n": 100,
        "source_n": 2000,
    },
    "en_sw": {
        "source_lang": "en",
        "target_lang": "sw",
        "source_corpus": "libritts",
        "target_corpus": "common_voice_sw",
        "source_mfa_dir": os.path.join(DATA_DIR, "mfa_output", "en"),
        "target_mfa_dir": os.path.join(DATA_DIR, "mfa_output", "sw"),
        "source_audio_dir": os.path.join(DATA_DIR, "audio", "en"),
        "target_audio_dir": os.path.join(DATA_DIR, "audio", "sw"),
        "target_train_n": 400,
        "target_test_n": 100,
        "source_n": 2000,
    },
}

# ============================================================
# Model hyperparameters (consistent across experiments)
# ============================================================
MODEL_CONFIG = {
    "d_model": 256,
    "n_heads": 4,
    "n_enc_layers": 4,
    "n_dec_layers": 4,
    "n_mels": 80,
    "dropout": 0.2,
    "postnet_channels": 256,
    "postnet_kernel": 5,
    "postnet_layers": 5,
}

TRAIN_CONFIG = {
    "batch_size": 32,
    "max_epochs": 300,
    "lr": 0.0005,
    "warmup_steps": 4000,
    "patience": 30,
    "val_ratio": 0.1,
    "grad_clip": 1.0,
}

# Alpha values for alpha-interpolation (Data Augmentation)
ALPHA_VALUES = [0.3, 0.4, 0.5, 0.6, 0.7]

# Target data sizes for ablation studies
ABLATION_SV_SIZES = [50, 100, 200, 300]

# Random seeds for result stability
SEEDS = [42, 123, 777]

# ============================================================
# Derived paths generator
# ============================================================
def get_paths(pair_name):
    """
    Returns a dictionary of paths where features, models, 
    and results will be stored for a specific language pair.
    """
    if pair_name not in LANGUAGE_PAIRS:
        raise ValueError(f"Language pair {pair_name} not defined in config.")
        
    pair = LANGUAGE_PAIRS[pair_name]
    # Output is organized by pair name (e.g., data/en_sw/)
    base = os.path.join(DATA_DIR, pair_name)
    
    return {
        "feat_dir": os.path.join(base, "features"),
        "cond_dir": os.path.join(base, "conditions"),
        "model_dir": os.path.join(PROJECT_DIR, "models", pair_name),
        "model_multiseed_dir": os.path.join(PROJECT_DIR, "models_multiseed", pair_name),
        "results_dir": os.path.join(PROJECT_DIR, "results", pair_name),
        "fig_dir": os.path.join(PROJECT_DIR, "results", pair_name, "figures"),
    }
