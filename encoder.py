import os
import numpy as np

class PlaylistEncoder():
    """
    Encodes the playlist into the 'training-set basis'. A playlist can only be represented with
    the tracks that are in the training set, as all other tracks are unknown to that playlist.
    """

    def __init__(self, tracks, accumulate):
        """
        Parameters
        ---
            tracks: the list of track ids used to encode a playlist.
        """
        self.mapping = {tid: i for i, (tid, *_) in enumerate(tracks)}
        self.accumulate = accumulate

    def __call__(self, tids):
        track_indices = [self.mapping[tid] for tid in tids if tid in self.mapping]
        encoding = np.zeros(len(self))
        for index, listens in zip(*np.unique(track_indices, return_counts=True)):
            encoding[index] = listens if self.accumulate else 1
        return encoding

    def __len__(self):
        return len(self.mapping)


class MelEncoder():
    def __init__(self, fp, length):
        self.fp = fp
        self.length = length

    def __call__(self, tid):
        mel = np.load(os.sep.join((self.fp, tid+'.npy')))
        tiled = np.tile(mel, (1, 1 + self.length // mel.shape[1]))
        return tiled[:,:self.length]

    def __len__(self):
        return self.length
