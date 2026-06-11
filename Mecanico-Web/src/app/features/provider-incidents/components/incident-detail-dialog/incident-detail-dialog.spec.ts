import { ComponentFixture, TestBed } from "@angular/core/testing";

import { IncidentDetailDialog } from "./incident-detail-dialog";

describe("IncidentDetailDialog", () => {
	let component: IncidentDetailDialog;
	let fixture: ComponentFixture<IncidentDetailDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [IncidentDetailDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(IncidentDetailDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
