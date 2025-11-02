// Rwanda Location Cascading Dropdown Handler
class LocationHandler {
    constructor() {
        this.locations = null;
        this.loadLocations();
    }

    async loadLocations() {
        try {
            const response = await fetch('../rwanda-locations-json-master/locations.json');
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            this.locations = await response.json();
            console.log('✅ Locations loaded successfully:', this.locations.provinces.length, 'provinces');
            this.initializeDropdowns();
        } catch (error) {
            console.error('❌ Error loading locations:', error);
            console.error('Current URL:', window.location.href);
            console.error('Trying to load from: ../rwanda-locations-json-master/locations.json');
            alert('Failed to load location data. Please refresh the page.\n\nError: ' + error.message);
        }
    }

    initializeDropdowns() {
        const provinceSelect = document.getElementById('provinceSelect');
        const districtSelect = document.getElementById('districtSelect');
        const sectorSelect = document.getElementById('sectorSelect');
        const cellSelect = document.getElementById('cellSelect');
        const villageSelect = document.getElementById('villageSelect');

        if (!provinceSelect || !districtSelect || !sectorSelect || !cellSelect || !villageSelect) {
            console.error('❌ Location dropdowns not found');
            return;
        }

        // Populate provinces
        this.populateProvinces();

        // Add event listeners for cascading
        provinceSelect.addEventListener('change', () => this.onProvinceChange());
        districtSelect.addEventListener('change', () => this.onDistrictChange());
        sectorSelect.addEventListener('change', () => this.onSectorChange());
        cellSelect.addEventListener('change', () => this.onCellChange());
    }

    populateProvinces() {
        const provinceSelect = document.getElementById('provinceSelect');
        provinceSelect.innerHTML = '<option value="">Select Province</option>';
        
        if (this.locations && this.locations.provinces) {
            this.locations.provinces.forEach(province => {
                const option = document.createElement('option');
                option.value = province.name;
                option.textContent = province.name;
                provinceSelect.appendChild(option);
            });
        }
    }

    onProvinceChange() {
        const provinceSelect = document.getElementById('provinceSelect');
        const districtSelect = document.getElementById('districtSelect');
        const sectorSelect = document.getElementById('sectorSelect');
        const cellSelect = document.getElementById('cellSelect');
        const villageSelect = document.getElementById('villageSelect');

        // Reset dependent dropdowns
        districtSelect.innerHTML = '<option value="">Select District</option>';
        sectorSelect.innerHTML = '<option value="">Select Sector</option>';
        cellSelect.innerHTML = '<option value="">Select Cell</option>';
        villageSelect.innerHTML = '<option value="">Select Village</option>';

        const selectedProvince = provinceSelect.value;
        if (!selectedProvince) return;

        const province = this.locations.provinces.find(p => p.name === selectedProvince);
        if (province && province.districts) {
            province.districts.forEach(district => {
                const option = document.createElement('option');
                option.value = district.name;
                option.textContent = district.name;
                districtSelect.appendChild(option);
            });
        }
    }

    onDistrictChange() {
        const provinceSelect = document.getElementById('provinceSelect');
        const districtSelect = document.getElementById('districtSelect');
        const sectorSelect = document.getElementById('sectorSelect');
        const cellSelect = document.getElementById('cellSelect');
        const villageSelect = document.getElementById('villageSelect');

        // Reset dependent dropdowns
        sectorSelect.innerHTML = '<option value="">Select Sector</option>';
        cellSelect.innerHTML = '<option value="">Select Cell</option>';
        villageSelect.innerHTML = '<option value="">Select Village</option>';

        const selectedProvince = provinceSelect.value;
        const selectedDistrict = districtSelect.value;
        if (!selectedProvince || !selectedDistrict) return;

        const province = this.locations.provinces.find(p => p.name === selectedProvince);
        if (province) {
            const district = province.districts.find(d => d.name === selectedDistrict);
            if (district && district.sectors) {
                district.sectors.forEach(sector => {
                    const option = document.createElement('option');
                    option.value = sector.name;
                    option.textContent = sector.name;
                    sectorSelect.appendChild(option);
                });
            }
        }
    }

    onSectorChange() {
        const provinceSelect = document.getElementById('provinceSelect');
        const districtSelect = document.getElementById('districtSelect');
        const sectorSelect = document.getElementById('sectorSelect');
        const cellSelect = document.getElementById('cellSelect');
        const villageSelect = document.getElementById('villageSelect');

        // Reset dependent dropdowns
        cellSelect.innerHTML = '<option value="">Select Cell</option>';
        villageSelect.innerHTML = '<option value="">Select Village</option>';

        const selectedProvince = provinceSelect.value;
        const selectedDistrict = districtSelect.value;
        const selectedSector = sectorSelect.value;
        if (!selectedProvince || !selectedDistrict || !selectedSector) return;

        const province = this.locations.provinces.find(p => p.name === selectedProvince);
        if (province) {
            const district = province.districts.find(d => d.name === selectedDistrict);
            if (district) {
                const sector = district.sectors.find(s => s.name === selectedSector);
                if (sector && sector.cells) {
                    sector.cells.forEach(cell => {
                        const option = document.createElement('option');
                        option.value = cell.name;
                        option.textContent = cell.name;
                        cellSelect.appendChild(option);
                    });
                }
            }
        }
    }

    onCellChange() {
        const provinceSelect = document.getElementById('provinceSelect');
        const districtSelect = document.getElementById('districtSelect');
        const sectorSelect = document.getElementById('sectorSelect');
        const cellSelect = document.getElementById('cellSelect');
        const villageSelect = document.getElementById('villageSelect');

        // Reset village dropdown
        villageSelect.innerHTML = '<option value="">Select Village</option>';

        const selectedProvince = provinceSelect.value;
        const selectedDistrict = districtSelect.value;
        const selectedSector = sectorSelect.value;
        const selectedCell = cellSelect.value;
        if (!selectedProvince || !selectedDistrict || !selectedSector || !selectedCell) return;

        const province = this.locations.provinces.find(p => p.name === selectedProvince);
        if (province) {
            const district = province.districts.find(d => d.name === selectedDistrict);
            if (district) {
                const sector = district.sectors.find(s => s.name === selectedSector);
                if (sector) {
                    const cell = sector.cells.find(c => c.name === selectedCell);
                    if (cell && cell.villages) {
                        cell.villages.forEach(village => {
                            const option = document.createElement('option');
                            option.value = village.name;
                            option.textContent = village.name;
                            villageSelect.appendChild(option);
                        });
                    }
                }
            }
        }
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new LocationHandler();
});
