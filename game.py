from src.objects import Game
import streamlit as st


game = Game("P1", "P2")
results = game.play()

print(results)
