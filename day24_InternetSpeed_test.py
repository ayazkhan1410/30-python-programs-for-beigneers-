'''
Day 24 of '30 days of 30
Programs challenege '''


# Python program to test

# internet speed
import speedtest

# Create a Speedtest object
s = speedtest.Speedtest()

# Get the best server to perform the test against
server = s.get_best_server()

# Get the ping of the connection
ping = s.ping()

# Get the download speed of the connection
download_speed = s.download()

# Get the upload speed of the connection
upload_speed = s.upload()

# Print the results
print("Ping:", ping, "ms")
print("Download speed:", download_speed / 1024 / 1024, "Mbps")
print("Upload speed:", upload_speed / 1024 / 1024, "Mbps")
