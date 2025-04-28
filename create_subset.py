import os
import shutil
import random
from pathlib import Path

# Define the mapping
MANIPULATION_TYPE_MAPPING = {
    0: 'pristine',
    1: 'face_audiomismatch_textmismatch',
    2: 'face_rvc_textmismatch',
    3: 'face_tts',
    4: 'face_tts_textgen',
    5: 'lip_audiomismatch_textmismatch',
    6: 'lip_rvc_textmismatch',
    7: 'lip_tts_textgen',
    8: 'rvc_textmismatch',
    9: 'tts_textgen',
    10: 'tts_textmismatch'
}

def create_subset(
    source_root=".",
    destination_root="./example_subset",
    split="train",
    num_ids=5,
    scenes_per_id=10,
    manipulation_type_ids=None,  # List of integers like [0,3,5]
    seed=42
):
    random.seed(seed)

    source_path = Path(source_root) / split
    destination_path = Path(destination_root) / split
    destination_path.mkdir(parents=True, exist_ok=True)

    if manipulation_type_ids is None:
        manipulation_types = [d.name for d in source_path.iterdir() if d.is_dir()]
    else:
        manipulation_types = [MANIPULATION_TYPE_MAPPING[mid] for mid in manipulation_type_ids]

    for manipulation in manipulation_types:
        src_manip_path = source_path / manipulation
        dst_manip_path = destination_path / manipulation

        if not src_manip_path.exists():
            print(f"Skipping missing manipulation type: {manipulation}")
            continue

        dst_manip_path.mkdir(parents=True, exist_ok=True)

        ids = [d.name for d in src_manip_path.iterdir() if d.is_dir()]
        if not ids:
            print(f"No IDs found under {src_manip_path}")
            continue

        selected_ids = random.sample(ids, min(num_ids, len(ids)))

        for id_ in selected_ids:
            src_id_path = src_manip_path / id_
            dst_id_path = dst_manip_path / id_
            dst_id_path.mkdir(parents=True, exist_ok=True)

            scenes = [d.name for d in src_id_path.iterdir() if d.is_dir()]
            if not scenes:
                print(f"No scenes found under {src_id_path}")
                continue

            selected_scenes = random.sample(scenes, min(scenes_per_id, len(scenes)))

            for scene in selected_scenes:
                src_scene_path = src_id_path / scene
                dst_scene_path = dst_id_path / scene
                if src_scene_path.is_dir():
                    shutil.copytree(src_scene_path, dst_scene_path)
                else:
                    print(f"Warning: {src_scene_path} is not a directory, skipped.")

    print(f"Subset created successfully at {destination_root}")

if __name__ == "__main__":
    # Example usage:
    create_subset(
        source_root=".",
        destination_root="./example_subset",
        split="train",
        num_ids=5,
        scenes_per_id=10,
        manipulation_type_ids=[0, 3, 8],  # Pick pristine, face_tts, rvc_textmismatch
        seed=42
    )
