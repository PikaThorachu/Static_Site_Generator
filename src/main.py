import os, shutil

def copy_src_to_public():
    src = 'static'
    dest = 'public'
    # Step 1 - Delete contents of public directory
    delete_public_contents(dest)
    # Step 2 - Move contents of static to public directory
    move_static_to_public(src, dest)

def delete_public_contents(dest):
        # Step 1: delete dest directory
        if os.path.exists(dest):
            shutil.rmtree(dest)
        # Step 2: create new dest directory
        os.mkdir(dest)
    

def move_static_to_public(src, dest):
    if os.path.exists(src):
        for item in os.listdir(src):
            item_src_path = os.path.join(src, item)
            item_dest_path = os.path.join(dest, item)
            if os.path.isfile(item_src_path):
                shutil.copy(item_src_path, item_dest_path)
                print(f"'{item_src_path}' has been copied to '{item_dest_path}'")
            if os.path.isdir(item_src_path):
                os.mkdir(item_dest_path)
                print(f"Directory '{item_dest_path}' has been created")
                move_static_to_public(item_src_path, item_dest_path)
    else:
        print("Source directory does not exist")
   
def main():
    copy_src_to_public()

main()
