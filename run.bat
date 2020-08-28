docker build -t emojiapp .

docker run --rm emojiapp python -m unittest

if %errorlevel% neq 0  exit /b

docker run --rm -it -p 5000:5000/UDP emojiapp
