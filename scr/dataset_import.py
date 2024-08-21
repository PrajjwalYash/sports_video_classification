import os
import requests
import patoolib
import shutil

def download_ucf101_dataset(download_url, download_path):
    """
    Download the UCF101 dataset from the provided URL.
    
    Args:
        download_url (str): The URL to download the dataset from.
        download_path (str): The local directory path where the dataset will be saved.
    """
    # Check if the download path exists, create it if not.
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # File path where the dataset will be downloaded.
    file_path = os.path.join(download_path, 'UCF101.rar')

    # Download the dataset with SSL verification disabled.
    response = requests.get(download_url, stream=True, verify=False)
    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # Filter out keep-alive new chunks.
                file.write(chunk)
    
    print(f"Dataset downloaded to {file_path}")
    return file_path

def extract_specific_classes(file_path, extract_to, classes_list):
    """
    Extract specific classes from the UCF101 dataset to the specified directory.
    
    Args:
        file_path (str): The path of the .rar file to extract.
        extract_to (str): The directory where the dataset will be extracted.
        classes_list (list): List of class names to extract.
    """
    # Temporary extraction path
    temp_extract_path = os.path.join(extract_to, 'temp')

    # Extract the entire dataset to a temporary location
    if not os.path.exists(temp_extract_path):
        os.makedirs(temp_extract_path)
    patoolib.extract_archive(file_path, outdir=temp_extract_path)
    print(f"Dataset extracted to temporary directory {temp_extract_path}")

    # Now move only the desired classes to the final directory
    for class_name in classes_list:
        class_dir = os.path.join(temp_extract_path, class_name)
        if os.path.exists(class_dir):
            shutil.move(class_dir, extract_to)
            print(f"Moved class {class_name} to {extract_to}")
        else:
            print(f"Class {class_name} not found in the dataset.")

    # Remove the temporary directory
    shutil.rmtree(temp_extract_path)
    print(f"Temporary directory {temp_extract_path} removed.")

if __name__ == "__main__":
    # URL of the UCF101 dataset.
    dataset_url = "https://www.crcv.ucf.edu/data/UCF101/UCF101.rar"
    
    # Directory to save the downloaded dataset.
    download_directory = "./UCF101"
    
    # Download the dataset.
    downloaded_file_path = download_ucf101_dataset(dataset_url, download_directory)
    
    # Directory to extract the dataset.
    extraction_directory = "./UCF101ActionRecog"
    
    # List of classes to extract
    CLASSES_LIST = ["SoccerJuggling", "SoccerPenalty", "Basketball", "BaseballPitch", "CricketBowling", "CricketShot"]
    
    # Extract only specific classes
    extract_specific_classes(downloaded_file_path, extraction_directory, CLASSES_LIST)
