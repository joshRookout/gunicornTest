def post_fork(server, worker):
    import rook
    rook.start(token='987cb968bd451072e2fae4ec9a3afa3741261cb58813059d1aa4daf122c9be49', labels={"env":"gunicorn-test"}, debug=1)
