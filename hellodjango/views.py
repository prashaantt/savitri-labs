from __future__ import division
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from nltk.tokenize import line_tokenize
import datetime
import nltk
import os
from nltk.corpus import PlaintextCorpusReader

def compare(request):
    errors = []
    statistics=[]
    stats=[]
    for x in range(1,3):
           cantoname = "canto"+str(x)+".txt"
           w=PlaintextCorpusReader("./",cantoname);
           w.words();
           t=nltk.text.Text(w.words());
           l_lines=len(line_tokenize(w.raw()))
           l_uwords=len(set(w.words()))
           l_words=len(w.words())
           l_sents=len(w.sents())
           l_paras=len(w.paras())
           l_linperpara=l_lines/l_paras
           statistics.append(x)
           statistics.append("Number of Words - "+ str(l_words))
           statistics.append("Number of Unique Words - "+ str(l_uwords))
           statistics.append("Number of Setences - "+ str(l_sents))
           statistics.append("Number of Lines - "+ str(l_lines))
           statistics.append("Number of Paras - "+ str(l_paras))
           statistics.append("Number of Lines/Paras - "+ str(l_linperpara))
           lexical_density=l_words/l_uwords
           l_wordpersent = l_words/l_sents
           statistics.append("Lexical Density (Total/Uniq) words- "+ str(lexical_density))
           statistics.append("Words per sentence - "+ str(l_wordpersent))
           stats.append(statistics)
           
    return render_to_response('compare.html', {'stats':statistics})
    

def stats(request):
    errors = []
    statistics=[]
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a Canto Number')
        else:
           cantoname = "canto"+q+".txt"
           w=PlaintextCorpusReader("./",cantoname);
           w.words();
           t=nltk.text.Text(w.words());
           l_lines=len(line_tokenize(w.raw()))
           l_uwords=len(set(w.words()))
           l_words=len(w.words())
           l_sents=len(w.sents())
           l_paras=len(w.paras())
           l_linperpara=l_lines/l_paras
           statistics.append("Number of Words - "+ str(l_words))
           statistics.append("Number of Unique Words - "+ str(l_uwords))
           statistics.append("Number of Setences - "+ str(l_sents))
           statistics.append("Number of Lines - "+ str(l_lines))
           statistics.append("Number of Paras - "+ str(l_paras))
           statistics.append("Number of Lines/Paras - "+ str(l_linperpara))
           lexical_density=l_words/l_uwords
           l_wordpersent = l_words/l_sents
           statistics.append("Lexical Density (Total/Uniq) words- "+ str(lexical_density))
           statistics.append("Words per sentence - "+ str(l_wordpersent))
           return render_to_response('stats.html', {'statistics':statistics})
    return render_to_response('stats.html', {'errors': errors})


def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})

def nlp(request):
	w=PlaintextCorpusReader("./","canto1.txt");
	w.words();
	t=nltk.text.Text(w.words())
	return render_to_response('lengths.html', {'word_length':len(set(w.words())), 'sentence_length' : len(w.sents())})

def search_form(request):
	if 'q' in request.GET:
		message = 'You searched for: %r' % request.GET['q']
	else:
		message = 'You submitted an empty form.'
	return render_to_response('search.html', {'query' : message})
   	

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search.html',
        {'errors': errors})