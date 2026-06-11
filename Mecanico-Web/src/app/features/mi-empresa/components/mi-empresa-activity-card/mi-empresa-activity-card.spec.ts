import { ComponentFixture, TestBed } from "@angular/core/testing";

import { MiEmpresaActivityCard } from "./mi-empresa-activity-card";

describe("MiEmpresaActivityCard", () => {
	let component: MiEmpresaActivityCard;
	let fixture: ComponentFixture<MiEmpresaActivityCard>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [MiEmpresaActivityCard],
		}).compileComponents();

		fixture = TestBed.createComponent(MiEmpresaActivityCard);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
