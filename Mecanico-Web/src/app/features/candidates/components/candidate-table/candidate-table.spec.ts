import { ComponentFixture, TestBed } from "@angular/core/testing";

import { CandidateTable } from "./candidate-table";

describe("CandidateTable", () => {
	let component: CandidateTable;
	let fixture: ComponentFixture<CandidateTable>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [CandidateTable],
		}).compileComponents();

		fixture = TestBed.createComponent(CandidateTable);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
