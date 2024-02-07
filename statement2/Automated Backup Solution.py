import os
import shutil
import boto3
from datetime import datetime

\
source_dir = "B:/dload" 
backup_dir ="B:/epic"
s3_bucket_name = "red" 
s3_backup_folder = "backups"  

def get_timestamp():
    now = datetime.now()
    return now.strftime("%Y-%m-%d_%H-%M-%S")


def create_local_backup():
    timestamp = get_timestamp()
    backup_filename = f"backup_{timestamp}.zip"
    backup_path = os.path.join(backup_dir, backup_filename)
    shutil.make_archive(backup_path.split('.zip')[0], 'zip', source_dir)
    return backup_path


def upload_to_s3(backup_path):
    s3 = boto3.client('s3')
    backup_filename = os.path.basename(backup_path)
    s3_key = f"{s3_backup_folder}/{backup_filename}"
    try:
        s3.upload_file(backup_path, s3_bucket_name, s3_key)
        return True
    except Exception as e:
        print(f"Failed to upload backup to S3: {str(e)}")
        return False


def main():
    try:
        backup_path = create_local_backup()
        if os.path.exists(backup_path):
            print("Local backup created successfully.")
            success = upload_to_s3(backup_path)
            if success:
                print("Backup uploaded to S3 successfully.")
            else:
                print("Failed to upload backup to S3.")
        else:
            print("Failed to create local backup.")
    except Exception as e:
        print(f"Backup failed: {str(e)}")


if __name__ == "__main__":
    main()
