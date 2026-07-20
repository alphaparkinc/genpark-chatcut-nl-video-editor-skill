class ChatCutNlVideoEditorClient:
    KEYWORD_OPERATIONS = {
        "pause": "REMOVE_SILENCE: Auto-detect and cut all pauses > 0.5s",
        "subtitle": "ADD_CAPTIONS: Generate word-level subtitles with speaker diarization",
        "b-roll": "INSERT_BROLL: Source and overlay contextual b-roll footage",
        "music": "ADD_MUSIC: Layer royalty-free background track at -18dB",
        "punchier": "SPEED_RAMP: Apply 1.15x speed on non-speech segments",
        "trim": "TRIM_EDGES: Remove first/last 2s of dead air",
        "graphic": "ADD_MOTION_GRAPHIC: Insert animated lower-third title card",
        "export": "EXPORT_TIMELINE: Package XML for Adobe Premiere / DaVinci Resolve"
    }

    def parse_instruction(self, edit_instruction: str, video_duration_sec: int) -> dict:
        instruction_lower = edit_instruction.lower()
        ops = []
        for keyword, operation in self.KEYWORD_OPERATIONS.items():
            if keyword in instruction_lower:
                ops.append(operation)
        if not ops:
            ops.append(f"ANALYZE: Process {video_duration_sec}s clip for general optimizations")
        export = "XML (Premiere/DaVinci)" if "export" in instruction_lower else "MP4 (Web-ready)"
        return {"edit_operations": ops, "export_format": export}
