# コンテストと問題の情報を取得
contest=$(basename "$(dirname "$PWD")")
problem=$(basename "$PWD")
problem_code="${contest:0:3}$problem"

# 解答を提出し、Pythonインタプリタを自動的に推測
echo "$problem_code" | acc submit -s -- --guess-python-interpreter pypy

# 次の問題ディレクトリに移動し、エディタを開く
next_problem=$(printf "\x$(printf "%x" $(( $(printf "%d" "'$problem") + 1 )) )")
cd "../$next_problem" && vs

