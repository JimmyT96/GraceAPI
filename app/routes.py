from flask import Blueprint, jsonify
import random

bp = Blueprint('api', _name_)

GRACE_VERSES = [
    {"reference": "Ephesians 2:8-9", "text": "For it is by grace you have been saved, through faith—and this is not from yourselves, it is the gift of God—not by works, so that no one can boast."},
    {"reference": "2 Corinthians 12:9", "text": "But he said to me, 'My grace is sufficient for you, for my power is made perfect in weakness.'"},
    {"reference": "Romans 3:23-24", "text": "For all have sinned and fall short of the glory of God, and all are justified freely by his grace through the redemption that came by Christ Jesus."},
    {"reference": "Titus 2:11", "text": "For the grace of God has appeared that offers salvation to all people."},
    {"reference": "Hebrews 4:16", "text": "Let us then approach God’s throne of grace with confidence, so that we may receive mercy and find grace to help us in our time of need."}
]

@bp.route('/')
def index():
    verse = random.choice(GRACE_VERSES)
    return jsonify({
        "service": "GraceAPI",
        "message": "Welcome to GraceAPI - serving God's grace",
        "verse_of_the_moment": verse,
        "conclusion": "The grace of God is sufficient for you today. His power is made perfect in weakness, and His love covers all. Walk in grace.",
        "author": "Jemimah",
        "endpoints": {
            "all_verses": "/api/v1/verses",
            "random_verse": "/api/v1/verse",
            "health": "/api/v1/health"
        }
    }), 200

@bp.route('/api/v1/verse')
def random_verse():
    return jsonify({
        "data": random.choice(GRACE_VERSES),
        "note": "His grace is sufficient for you."
    }), 200

@bp.route('/api/v1/verses')
def all_verses():
    return jsonify({
        "count": len(GRACE_VERSES),
        "theme": "grace",
        "verses": GRACE_VERSES,
        "summary": "Each verse testifies: the grace of God is sufficient, unearned, and available to all through Christ."
    }), 200

@bp.route('/api/v1/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "GraceAPI",
        "uptime_message": "Sustained by grace",
        "maintainer": "Jemimah"
    }), 200

