import ACEScg_convertor

toolbar = nuke.menu('Nodes')
aaMenu = toolbar.addMenu('ACES', 'A_logo.png')

aaMenu.addCommand('ACEScg', 'ACEScg_convertor.to_ACEScg()', 'a')
