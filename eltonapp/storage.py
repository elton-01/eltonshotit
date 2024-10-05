# eltonapp/supabase_storage.py

# from django.core.files.storage import Storage
# from supabase import create_client, Client
# import os



# from django.core.files.storage import Storage
# from supabase import create_client
# from django.conf import settings

# class SupabaseStorage(Storage):
#     def __init__(self):
#         url = "https://bxtduxfeqfrnbmchbehq.supabase.co"
#         # anon
#         key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ4dGR1eGZlcWZybmJtY2hiZWhxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjY0MDg3NTIsImV4cCI6MjA0MTk4NDc1Mn0.ZosYNZVv5XdIYT_jafLohnps_m-GPyxGo2jT7GW2Dg4"
#         # key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ4dGR1eGZlcWZybmJtY2hiZWhxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNjQwODc1MiwiZXhwIjoyMDQxOTg0NzUyfQ.U7XfOEXOBZ3bBkoyNHkXZLWTY_yGsDC1Yl_rCQ3-FxQ"
#         self.supabase = create_client(url, key)

#     def _save(self, name, content):
#         # Upload the file to Supabase
#         file_data = content.read()
#         response = self.supabase.storage.from_("eltonshotit").upload(name, file_data)

#         if response.error:
#             raise Exception(f"Error uploading file: {response.error}")

#         return name

#     def url(self, name):
#         return f"https://bxtduxfeqfrnbmchbehq.supabase.co/storage/v1/object/public/eltonshotit/{name}"





# # storage.py
# from django.core.files.storage import Storage
# from django.core.exceptions import ImproperlyConfigured
# from supabase import create_client
# import mimetypes
# import os




# class SupabaseStorage(Storage):
#     def __init__(self):
#         # Initialize with the Supabase credentials
#         self.supabase_url = "https://bxtduxfeqfrnbmchbehq.supabase.co"
#         self.supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ4dGR1eGZlcWZybmJtY2hiZWhxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjY0MDg3NTIsImV4cCI6MjA0MTk4NDc1Mn0.ZosYNZVv5XdIYT_jafLohnps_m-GPyxGo2jT7GW2Dg4"
        
#         if not self.supabase_url or not self.supabase_key:
#             raise ImproperlyConfigured("Supabase credentials are missing")
        
#         self.supabase = create_client(self.supabase_url, self.supabase_key)

#     def _save(self, name, content):
#         """Upload file to Supabase Storage."""
#         bucket_name = "eltonshotit"
#         file_extension = os.path.splitext(name)[1]
#         mime_type = mimetypes.guess_type(name)[0]

#         response = self.supabase.storage.from_(bucket_name).upload(name, content.read(), {
#             "content-type": mime_type or "application/octet-stream"
#         })
        
#         if response.get("error"):
#             raise Exception(f"Error uploading file: {response['error']['message']}")
        
#         return name

#     def exists(self, name):
#         """Check if the file exists in Supabase Storage."""
#         bucket_name = "eltonshotit"
#         file_data = self.supabase.storage.from_(bucket_name).get_public_url(name)
#         return file_data is not None

#     def url(self, name):
#         """Get the public URL for the file."""
#         bucket_name = "eltonshotit"
#         response = self.supabase.storage.from_(bucket_name).get_public_url(name)
#         if response.get("error"):
#             raise Exception(f"Error getting URL: {response['error']['message']}")
#         return response['publicURL']

#     def delete(self, name):
#         """Delete the file from Supabase Storage."""
#         bucket_name = "eltonshotit"
#         response = self.supabase.storage.from_(bucket_name).remove([name])
#         if response.get("error"):
#             raise Exception(f"Error deleting file: {response['error']['message']}")

#     def _open(self, name, mode='rb'):
#         """Not implemented."""
#         raise NotImplementedError("Supabase storage does not support opening files directly.")

#     def size(self, name):
#         """Not implemented."""
#         raise NotImplementedError("Size check is not implemented for Supabase Storage.")

#     def test_connection(self):
#         """Test the connection to Supabase Storage."""
#         try:
#             self.supabase.storage.list_buckets()
#             print("Connection to Supabase is successful.")
#         except Exception as e:
#             print(f"Failed to connect to Supabase: {e}")


import mimetypes
import os
import requests
from django.core.files.storage import Storage
from django.core.exceptions import ImproperlyConfigured

class SupabaseStorage(Storage):
    def __init__(self):
        # Initialize with the Supabase credentials
        self.supabase_url = "https://bxtduxfeqfrnbmchbehq.supabase.co"
        self.supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ4dGR1eGZlcWZybmJtY2hiZWhxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNjQwODc1MiwiZXhwIjoyMDQxOTg0NzUyfQ.U7XfOEXOBZ3bBkoyNHkXZLWTY_yGsDC1Yl_rCQ3-FxQ"  # Make sure to use your actual Supabase key
        
        if not self.supabase_url or not self.supabase_key:
            raise ImproperlyConfigured("Supabase credentials are missing")

    def _save(self, name, content):
        """Upload file to Supabase Storage."""
        bucket_name = "eltonshotit"
        url = f"{self.supabase_url}/storage/v1/object/public/{bucket_name}/{name}"
        
        mime_type = mimetypes.guess_type(name)[0] or "application/octet-stream"

        headers = {
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": mime_type,
        }

        response = requests.put(url, headers=headers, data=content.read())
        
        if response.status_code != 200:
            raise Exception(f"Error uploading file: {response.text}")

        return name

    def exists(self, name):
        """Check if the file exists in Supabase Storage."""
        bucket_name = "eltonshotit"
        url = f"{self.supabase_url}/storage/v1/object/public/{bucket_name}/{name}"
        
        response = requests.head(url)
        return response.status_code == 200

    def url(self, name):
        """Get the public URL for the file."""
        bucket_name = "eltonshotit"
        return f"{self.supabase_url}/storage/v1/object/public/{bucket_name}/{name}"

    def delete(self, name):
        """Delete the file from Supabase Storage."""
        bucket_name = "eltonshotit"
        url = f"{self.supabase_url}/storage/v1/object/{bucket_name}/{name}"
        
        headers = {
            "Authorization": f"Bearer {self.supabase_key}",
        }

        response = requests.delete(url, headers=headers)
        
        if response.status_code != 204:
            raise Exception(f"Error deleting file: {response.text}")

    def _open(self, name, mode='rb'):
        """Not implemented."""
        raise NotImplementedError("Supabase storage does not support opening files directly.")

    def size(self, name):
        """Not implemented."""
        raise NotImplementedError("Size check is not implemented for Supabase Storage.")
