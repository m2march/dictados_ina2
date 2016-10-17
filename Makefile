.PHONY: pdf midi

N = 31
PDF = $(N).pdf
MIDI = $(N).mid
ABC = $(N).abc
MP3 = $(N).mp3

pdf: $(PDF)
	evince $<

midi: $(MIDI)
	timidity $<

mp3: $(MP3)
	mplayer $<

$(PDF): $(ABC)
	python abc2pdf.py $<

$(MIDI): $(ABC)
	abc2midi $< -o $@
