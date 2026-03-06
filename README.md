# Phoneme_data_augmentation

## Methods
Condition A — Target-only baseline

Condition B — Raw source mixture

Condition C (Global Δ) — Global mean shift

Condition C (Phoneme Δ) 

Condition F — Phoneme-level interpolation
```
mel_aug[phone] = (1 - α) · mel_src[phone] + α · μ_tgt[phone]
```
