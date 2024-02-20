from ipytv import playlist
import sys

path='mahendra.m3u'

def safeOpen(path, mode):
  try:
    openFile = open(path, mode)
  except:
    sys.exit("ERROR: Could not open " + path)
  return openFile

def channel_count(f):
  pl = playlist.loadf(f)
  return print(f'There are {pl.length()} channels.')

def list_channels(f, o):
  outfile = safeOpen(o, 'w')
  channel_list = []
  pl = playlist.loadf(f)
  for channel in pl:
    outfile.write(channel.name)
    outfile.write('\n')
  outfile.close()