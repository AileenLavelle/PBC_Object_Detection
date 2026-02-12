# Hard Cases for Annotation - Summary Report
Generated: 2026-02-12 08:56:41

## Overview
- Total images analyzed: 2625
- Already labeled: 732
- Unlabeled: 1893

## Priority Folders

### 1_high_priority (50 images)
These are the MOST VALUABLE images to annotate. They include:
- Unlabeled images where model is uncertain
- Images with no detections (might have vessels we're missing)
- Images with low-confidence detections

### 2_medium_priority (50 images)
These are also valuable but slightly lower priority.

### 3_unlabeled_with_detections (30 images)
These are unlabeled images where the model found vessels with HIGH confidence.
The model's predictions are likely correct, so annotation should be quick.
Good for quickly expanding the dataset.

### 4_model_missing_vessels (20 images)
These are ALREADY LABELED images where the model predicts FEWER vessels 
than the ground truth. Worth reviewing to understand what the model misses.

## Recommendations
1. Start with 1_high_priority folder
2. Focus on variety: different lighting, weather, vessel sizes
3. For 3_unlabeled_with_detections: verify model predictions are correct, then approve
4. Review 4_model_missing_vessels to understand failure cases

## Current Model Performance
- mAP50: 0.8791
- Target: 0.90+ (need ~200+ more annotated images)
