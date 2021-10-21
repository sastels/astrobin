from astrobin_apps_equipment.api.filters.equipment_item_edit_proposal_filter import EquipmentItemEditProposalFilter
from astrobin_apps_equipment.models.sensor_edit_proposal import SensorEditProposal


class SensorEditProposalFilter(EquipmentItemEditProposalFilter):
    class Meta(EquipmentItemEditProposalFilter.Meta):
        model = SensorEditProposal
