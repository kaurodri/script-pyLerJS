import subprocess

def run_js_file(js_file):
    process = subprocess.Popen(['node', js_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()

js_file = "index.js"
output, error = run_js_file(js_file)
print("Output:", output)
print("Error:", error)