import moviepy.editor as mp
from src.stt.stt import stt_from_audio
from src.translator.text_to_gloss import text_to_gloss
from src.video.extract_poses import extract_poses
import subprocess

def generate_sign_video(audio_file, output_path):
    text = stt_from_audio(audio_file)
    gloss = text_to_gloss(text)
    reference_video = f'data/signs/{gloss}.mp4'
    pose_path = f'data/poses/{gloss}_poses.npy'
    extract_poses(reference_video, pose_path)
    video_path = f'data/videos/{gloss}.mp4'
    subprocess.run(['blender', '--background', '--python', 'src/video/blender_animate.py'])
    animated_clip = mp.VideoFileClip(video_path)
    audio_clip = mp.AudioFileClip(audio_file)
    final_video = animated_clip.set_audio(audio_clip)
    final_video.write_videofile(output_path, fps=30)
    return output_path