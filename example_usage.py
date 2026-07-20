from client import ChatCutNlVideoEditorClient
client = ChatCutNlVideoEditorClient()
result = client.parse_instruction(
    edit_instruction="Remove all pauses, add subtitles, insert b-roll and make it punchier",
    video_duration_sec=180
)
print(f"Export: {result['export_format']}")
print("Edit operations:")
for op in result["edit_operations"]:
    print(f"  -> {op}")
