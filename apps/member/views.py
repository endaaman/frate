# -*- encoding:utf-8 -*-
from django.shortcuts import render, render_to_response
from models import Member
from django.template import RequestContext
import datetime


def home(request):
    members = []
    d = datetime.datetime.today()
    for i in reversed(range(12)):
        # 2013 4~12 なら 2013入学は一年目
        # 2013 1~3 なら 2012入学は一年目
        base_year = d.year if d.month > 3 else d.year - 1
        # (i: 5~1)
        y = base_year - i
        ms = Member.objects.filter(join_year=y)
        mss = []
        for m in ms:
            if m.grade() < 7:
                mss.append(m)
        if len(mss) > 0:
            members.append(mss)

    return render_to_response('member/home.html',
                              dict(
                                  members=members,
                                  r=[i + 1 for i in range(6)]
                              ),
                              context_instance=RequestContext(request))

