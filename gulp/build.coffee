

g.task 'build', [
    'copy'
    'html:build'
    'js:build'
    'css:build'
    'clean:cache'
    'index'
]
