"""Liftbot API Routes."""

from flask import Blueprint, request, jsonify

# Define Blueprint
liftbot_bp = Blueprint("liftbot", __name__, url_prefix="/api/liftbot")