import { ComponentFixture, TestBed } from "@angular/core/testing";

import { CandidateDetailDialog } from "./candidate-detail-dialog";

describe("CandidateDetailDialog", () => {
	let component: CandidateDetailDialog;
	let fixture: ComponentFixture<CandidateDetailDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [CandidateDetailDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(CandidateDetailDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
