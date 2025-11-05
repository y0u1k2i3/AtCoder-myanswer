FROM pypy:3.10-7.3.12

# 必要なパッケージを一括インストール
RUN apt update && \
    apt-get install -y --no-install-recommends \
    zsh time tzdata tree git curl wget bzip2 gcc g++ gfortran \
    libopenblas-dev libatlas-base-dev liblapack-dev pkg-config \
    libgeos-dev nodejs npm clang dirmngr ca-certificates \
    software-properties-common apt-transport-https ruby-full \
    build-essential gdb lcov libbz2-dev libffi-dev libgdbm-dev \
    libgdbm-compat-dev liblzma-dev libncurses5-dev libreadline6-dev \
    libsqlite3-dev libssl-dev lzma lzma-dev tk-dev uuid-dev zlib1g-dev \
    expect \
    && rm -rf /var/lib/apt/lists/*v\
    && apt-get clean

# 設定ファイルのコピー
COPY ./requirements.txt ./.zshrc /tmp/

# Pythonパッケージのインストール
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r /tmp/requirements.txt

# AtCoder CLIのインストールと設定
RUN npm install -g atcoder-cli && \
    acc config default-task-choice all && \
    mkdir -p $(acc config-dir)/py && \
    touch $(acc config-dir)/py/main.py && \
    echo '{"task":{"program": ["main.py"],"submit": "main.py"}}' > $(acc config-dir)/py/template.json && \
    acc config default-template py && \
    acc templates

# スクリプトファイルを配置し、実行権限を付与
COPY ./login.sh ./init_contest.sh ./init_practice.sh ./submit.sh ./submit_safe.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/*.sh

# zinitのインストール
RUN zsh -c "$(curl --fail --show-error --silent --location https://raw.githubusercontent.com/zdharma-continuum/zinit/HEAD/scripts/install.sh)"

# .zshrcの内容をユーザーの.zshrcに追加
RUN cat /tmp/.zshrc >> $HOME/.zshrc
