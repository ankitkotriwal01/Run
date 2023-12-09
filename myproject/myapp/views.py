from django.shortcuts import render
# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
import streamlit as st
import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
# Your black_scholes_call function remains the same

def streamlit_view(request):
    if request.method == 'POST':
        S = float(request.POST.get('S'))
        K = float(request.POST.get('K'))
        T = float(request.POST.get('T'))
        r = float(request.POST.get('r'))
        sigma = float(request.POST.get('sigma'))
        option_value = black_scholes_call(S, K, T, r, sigma)
        return HttpResponse(f"The value of the call option is: {option_value:.2f}")

    return render(request, 'streamlit_template.html')

def main():
    st.title("Call Option Value Calculator")
    # Your Streamlit code remains the same

if __name__ == "__main__":
    main()

# Create your views here.
