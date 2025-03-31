import os

# Root folder path
root_folder = "squares"

for i in range(1, 109):
    root_folder = "squares" + "/" + str(i)
    print(root_folder)
    files_with_timestamps = []
    for dirpath, _, filenames in os.walk(root_folder):

        for filename in filenames:
            print(filename)
            if filename.endswith(".png"):  # Only process PNG files
                old_file_path = os.path.join(dirpath, filename)
                # Extract timestamp from filename
                timestamp_str = filename.split(" ")[1]  # Extract "2025-01-03 030803"
                timestamp = int(timestamp_str.replace(".png", "").replace(" ", "").replace("-", "").replace(":", ""))
                files_with_timestamps.append((old_file_path, timestamp))


    # Sort files by timestamp
    files_with_timestamps.sort(key=lambda x: x[1])  # Sort by the extracted timestamp

    # Rename files based on order
    new_names = ["sumerian.png", "chinese.png"]
    for (old_file_path, _), new_name in zip(files_with_timestamps, new_names):
        
        if len(files_with_timestamps) > 2:
            continue
        
        dirpath = os.path.dirname(old_file_path)
        new_file_path = os.path.join(dirpath, new_name)
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {old_file_path} -> {new_file_path}")
