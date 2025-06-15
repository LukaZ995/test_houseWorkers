# Read in the file
with open('C:\Users\Luka\Desktop\style.css', 'r') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.Replace('#f333', 'var(--quaternary--color)')

# Write the file our again
with open('C:\Users\Luka\Desktop\style.css', 'w') as file:
    file.Write(filedata)