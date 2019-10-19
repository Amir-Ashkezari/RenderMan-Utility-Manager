import nuke
import os

def to_ACEScg():
    selNodes = nuke.selectedNodes()
    for node in selNodes:
        bitDepth = node.metadata('input/bitsperchannel')
        if bitDepth == '8-bit fixed' or bitDepth == '16-bit fixed':
            node['colorspace'].setValue(137)
            fileParm = node['file'].value()
            wNode = nuke.nodes.Write()
            wNode.setInput(0, node)
            fileName = str(fileParm.split('/')[-1])
            newName = str(fileName.split('.')[0] + '_ACEScg')
            fileName = fileName.replace(str(fileName.split('.')[0]), newName)
            filename, fileExt = os.path.splitext(fileName)
            newFileName = filename + '.exr'
            newPath = fileParm.replace(str(fileParm.split('/')[-1]), newFileName)
            wNode['file'].setValue(newPath)
            wNode['file_type'].setValue(3)
            wNode['colorspace'].setValue(5)
            wNode['write_ACES_compliant_EXR'].setValue(1)
            nuke.execute(wNode,start=1,end=1,incr=1)
        elif bitDepth == '16-bit half float' or bitDepth == '32-bit float':
            node['colorspace'].setValue(131)
            fileParm = node['file'].value()
            wNode = nuke.nodes.Write()
            wNode.setInput(0, node)
            fileName = str(fileParm.split('/')[-1])
            newName = str(fileName.split('.')[0] + '_ACEScg')
            fileName = fileName.replace(str(fileName.split('.')[0]), newName)
            filename, fileExt = os.path.splitext(fileName)
            newFileName = filename + '.exr'
            newPath = fileParm.replace(str(fileParm.split('/')[-1]), newFileName)
            wNode['file'].setValue(newPath)
            wNode['file_type'].setValue(3)
            wNode['colorspace'].setValue(5)
            wNode['write_ACES_compliant_EXR'].setValue(1)
            nuke.execute(wNode,start=1,end=1,incr=1)