import bpy

def select_bones_by_suffix(bone_suffixes):
    bpy.ops.object.mode_set(mode='EDIT')
    armature = bpy.context.object.data

    for bone in armature.edit_bones:
        for suffix in bone_suffixes:
            if bone.name.endswith(suffix):
                bone.select = True

def invert_selection():
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.armature.select_all(action='INVERT')

def delete_selected_bones():
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.armature.delete()

def switch_to_object_mode():
    bpy.ops.object.mode_set(mode='OBJECT')

# Usage example
bone_list = '''
_Head
_Hips
_LArm
_LArmBendHalf
_LArmRoll
_LArmRollHalf
_LFoot
_LForeArm
_LForeArmBendHalf
_LHand
_LHandBendHalf
_LHandElbowSub1
_LHandElbowSub2
_LHandIndex_01
_LHandIndex_02
_LHandIndex_03
_LHandMiddle_01
_LHandMiddle_02
_LHandMiddle_03
_LHandPinky_01
_LHandPinky_02
_LHandPinky_03
_LHandRing_01
_LHandRing_02
_LHandRing_03
_LHandRoll
_LHandRollHalf
_LHandRollHalf2
_LHandThumb_01
_LHandThumb_02
_LHandThumb_03
_LKneeSub
_LLegBendHalf
_LLegSlide
_LShoulder
_LToeBase
_LUpLeg
_LUpLegBendHalf
_LUpLegRoll
_LUpLegRollHalf
_LUpLegSideSub
_Neck
_RArm
_RArmBendHalf
_RArmRoll
_RArmRollHalf
_RFoot
_RForeArm
_RForeArmBendHalf
_RHand
_RHandBendHalf
_RHandElbowSub1
_RHandElbowSub2
_RHandIndex_01
_RHandIndex_02
_RHandIndex_03
_RHandMiddle_01
_RHandMiddle_02
_RHandMiddle_03
_RHandPinky_01
_RHandPinky_02
_RHandPinky_03
_RHandRing_01
_RHandRing_02
_RHandRing_03
_RHandRoll
_RHandRollHalf
_RHandRollHalf2
_RHandThumb_01
_RHandThumb_02
_RHandThumb_03
_RKneeSub
_RLegBendHalf
_RLegSlide
_RShoulder
_RToeBase
_RUpLeg
_RUpLegBendHalf
_RUpLegRoll
_RUpLegRollHalf
_RUpLegSideSub
_SP_LBreast
_SP_RBreast
_Spine_01
_Spine_02
_Spine_03
'''

# Convert the bone_list string to a list of bone suffixes
bone_suffixes = bone_list.strip().split('\n')

# Select bones based on the suffixes
select_bones_by_suffix(bone_suffixes)

# Invert the selection
invert_selection()

# Delete the selected bones
delete_selected_bones()

# Switch back to object mode
switch_to_object_mode()
