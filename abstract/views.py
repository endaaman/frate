#-*-encoding:utf-8-*-
from django import forms

class MessageBaseForm(forms.ModelForm):
    class Meta:
        exclude = ('message_html', 'raw_message',)
        help_texts = {
            'message': '本文には<a href="%s" target="_blank">Markdown記法</a>が使えます。'
                       # % urlresolvers.reverse('blog.show', args=('markdown', ))
                       % '/blog/markdown/'
            ,
        }
