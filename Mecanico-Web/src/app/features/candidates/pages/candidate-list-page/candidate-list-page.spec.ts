import { ComponentFixture, TestBed } from "@angular/core/testing";

import { CandidateListPage } from "./candidate-list-page";

describe("CandidateListPage", () => {
	let component: CandidateListPage;
	let fixture: ComponentFixture<CandidateListPage>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [CandidateListPage],
		}).compileComponents();

		fixture = TestBed.createComponent(CandidateListPage);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
