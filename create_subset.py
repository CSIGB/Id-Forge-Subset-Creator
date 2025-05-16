            continue

        identity_folders = [d.name for d in src_manip_path.iterdir() if d.is_dir()]
        if not identity_folders:
            print(f"⚠️ No identities found in: {src_manip_path}")
            continue

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
                    print(f"⚠️ No scenes in video: {src_video_path}")
                    continue

                selected_scene_folders = random.sample(scene_folders, min(scenes_per_video, len(scene_folders)))

                for scene_folder in selected_scene_folders:
                    src_scene_path = src_video_path / scene_folder
                    dst_scene_path = dst_video_path / scene_folder
                    if src_scene_path.exists():
                        shutil.copytree(src_scene_path, dst_scene_path)
                    else:
                        print(f"❌ Scene folder does not exist: {src_scene_path}")

    print(f"\n✅ Subset created successfully at: {destination_split_path}\n")

if __name__ == "__main__":
    main()
