import os
import random
import shutil
from pathlib import Path

# Mapping integer codes to manipulation type folder names
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
    10: 'tts_textmismatch',
}

def create_subset(
    source_root=".",
    destination_root="./example_subset",
    split="train",
    num_ids=5,
    videos_per_id=2,
    scenes_per_video=10,
    manipulation_type_ids=None,
    seed=42
):
    random.seed(seed)

    source_split_path = Path(source_root) / split
    destination_split_path = Path(destination_root) / split
    destination_split_path.mkdir(parents=True, exist_ok=True)

    # Get manipulation types
    if manipulation_type_ids is None:
        manipulation_types = [d.name for d in source_split_path.iterdir() if d.is_dir()]
    else:
        manipulation_types = [MANIPULATION_TYPE_MAPPING[mid] for mid in manipulation_type_ids]

    for manipulation_type in manipulation_types:
        src_manip_path = source_split_path / manipulation_type
        dst_manip_path = destination_split_path / manipulation_type
        dst_manip_path.mkdir(parents=True, exist_ok=True)

        identity_folders = [d.name for d in src_manip_path.iterdir() if d.is_dir()]
        selected_identities = random.sample(identity_folders, min(num_ids, len(identity_folders)))

        for identity in selected_identities:
            src_identity_path = src_manip_path / identity
            dst_identity_path = dst_manip_path / identity
            dst_identity_path.mkdir(parents=True, exist_ok=True)

            video_folders = [d.name for d in src_identity_path.iterdir() if d.is_dir()]
            selected_video_folders = random.sample(video_folders, min(videos_per_id, len(video_folders)))

            for video_name in selected_video_folders:
                src_video_path = src_identity_path / video_name
                dst_video_path = dst_identity_path / video_name
                dst_video_path.mkdir(parents=True, exist_ok=True)

                scene_folders = [d.name for d in src_video_path.iterdir() if d.is_dir()]
                if not scene_folders:
                    continue

                selected_scene_folders = random.sample(scene_folders, min(scenes_per_video, len(scene_folders)))

                for scene_folder in selected_scene_folders:
                    src_scene_path = src_video_path / scene_folder
                    dst_scene_path = dst_video_path / scene_folder
                    shutil.copytree(src_scene_path, dst_scene_path)

    print(f"\n✅ Subset created successfully at: {destination_split_path}\n")
