import { ComponentFixture, TestBed } from "@angular/core/testing";

import { MiEmpresaMetricsCard } from "./mi-empresa-metrics-card";

describe("MiEmpresaMetricsCard", () => {
	let component: MiEmpresaMetricsCard;
	let fixture: ComponentFixture<MiEmpresaMetricsCard>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [MiEmpresaMetricsCard],
		}).compileComponents();

		fixture = TestBed.createComponent(MiEmpresaMetricsCard);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
