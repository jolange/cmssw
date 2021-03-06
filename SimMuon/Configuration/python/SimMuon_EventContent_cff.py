# The following comments couldn't be translated into the new config version:

#save digis

#save digis sim link and trigger infos

import FWCore.ParameterSet.Config as cms

# Used to make conditional changes for different running scenarios
from Configuration.StandardSequences.Eras import eras

#Full Event content with DIGI
SimMuonFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_simMuonCSCDigis_*_*', 
        'keep *_simMuonDTDigis_*_*', 
        'keep *_simMuonRPCDigis_*_*')
)
#RAW content
SimMuonRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*')
)
# Add extra collections if running in Run 2. Not sure why but these
# collections were added to pretty much all event content in the old
# customisation function.
eras.run2_common.toModify( SimMuonRAW.outputCommands, func=lambda outputCommands: outputCommands.append('keep *_simMuonCSCDigis_*_*') )
eras.run2_common.toModify( SimMuonRAW.outputCommands, func=lambda outputCommands: outputCommands.append('keep *_simMuonRPCDigis_*_*') )

#RECO content
SimMuonRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*')
)
#AOD content
SimMuonAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

def _modifySimMuonEventContentFEVTDEBUGForPhase2( object ):
    object.outputCommands.append('keep *_simMuonGEMDigis_*_*')
    object.outputCommands.append('keep *_simMuonGEMPadDigis_*_*')
    object.outputCommands.append('keep *_simMuonME0Digis_*_*')

def _modifySimMuonEventContentRAWRECOForPhase2( object ):
    object.outputCommands.append('keep StripDigiSimLinkedmDetSetVector_simMuonGEMDigis_*_*')

from Configuration.StandardSequences.Eras import eras
eras.phase2_muon.toModify( SimMuonFEVTDEBUG, func=_modifySimMuonEventContentFEVTDEBUGForPhase2 )
eras.phase2_muon.toModify( SimMuonRAW, func=_modifySimMuonEventContentRAWRECOForPhase2 )
eras.phase2_muon.toModify( SimMuonRECO, func=_modifySimMuonEventContentRAWRECOForPhase2 )
